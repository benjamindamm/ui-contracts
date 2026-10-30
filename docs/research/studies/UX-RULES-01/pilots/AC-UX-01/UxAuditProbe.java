import java.nio.file.*;
import java.io.*;
import java.util.*;
import com.fasterxml.jackson.databind.*;
import org.camunda.dmn.DmnEngine;

class UxAuditProbe {
 static Object normalize(Object value){
  if(value==null)return null;
  if(value instanceof scala.Option<?> o)return o.isDefined()?normalize(o.get()):null;
  if(value instanceof scala.collection.Map<?,?> map){Map<String,Object> out=new LinkedHashMap<>();var it=map.iterator();while(it.hasNext()){var e=it.next();out.put(String.valueOf(e._1()),normalize(e._2()));}return out;}
  if(value instanceof scala.collection.Iterable<?> list){List<Object> out=new ArrayList<>();var it=list.iterator();while(it.hasNext())out.add(normalize(it.next()));return out;}
  if(value instanceof String||value instanceof Number||value instanceof Boolean)return value;
  return value.toString();
 }
 public static void main(String[] args)throws Exception{
  ObjectMapper json=new ObjectMapper();Map<String,Object> request=json.readValue(System.in,Map.class);
  DmnEngine engine=new DmnEngine.Builder().build();
  Map<String,Object> result=new LinkedHashMap<>();
  try(InputStream file=Files.newInputStream(Path.of(args[0]))){
   var parsed=engine.parse(file);
   if(parsed.isLeft()){result.put("stage","parse-error");result.put("error",parsed.left().get().toString());}
   else{var evaluated=engine.eval(parsed.toOption().get(),args[1],request);
    if(evaluated.isLeft()){result.put("stage","evaluation-error");result.put("error",evaluated.left().get().toString());}
    else{result.put("stage","evaluated");result.put("value",normalize(evaluated.toOption().get().value()));
     List<Object> trace=new ArrayList<>();var logs=evaluated.toOption().get().auditLog().entries().iterator();
     while(logs.hasNext()){var entry=logs.next();Map<String,Object> item=new LinkedHashMap<>();item.put("decisionId",entry.id());item.put("name",entry.name());List<String> matched=new ArrayList<>();
      if(entry.result() instanceof org.camunda.dmn.Audit.DecisionTableEvaluationResult table){var rows=table.matchedRules().iterator();while(rows.hasNext())matched.add(rows.next().rule().id());}
      item.put("matchedRowIds",matched);trace.add(item);
     }result.put("trace",trace);}
   }
  }
  System.out.println(json.writeValueAsString(result));
 }
}
