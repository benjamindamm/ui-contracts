import { useModel as _useModel, defineComponent as _defineComponent } from 'vue'
import { unref as _unref, createVNode as _createVNode, withCtx as _withCtx, openBlock as _openBlock, createBlock as _createBlock } from "vue"

import { computed } from 'vue';
import { SliderRange, SliderRoot, SliderThumb, SliderTrack } from 'reka-ui';


const ResearchGenerated = /*@__PURE__*/_defineComponent({
  __name: 'quarter',
  props: {
    "value": { type: Number, ...{ default: 25 } },
    "valueModifiers": {},
  },
  emits: ["update:value"],
  setup(__props) {

const value = _useModel<number>(__props, 'value');

const values = computed({
  get: () => [value.value],
  set: (next: number[] | undefined) => {
    value.value = next?.[0] ?? value.value;
  }
});

return (_ctx: any,_cache: any) => {
  return (_openBlock(), _createBlock(_unref(SliderRoot), {
    min: 0,
    max: 100,
    step: 1,
    class: "research-slider",
    modelValue: values.value,
    "onUpdate:modelValue": _cache[0] || (_cache[0] = ($event: any) => ((values).value = $event))
  }, {
    default: _withCtx(() => [
      _createVNode(_unref(SliderTrack), { class: "research-slider__track" }),
      _createVNode(_unref(SliderRange), { class: "research-slider__range" }),
      _createVNode(_unref(SliderThumb), { class: "research-slider__thumb" })
    ]),
    _: 1 /* STABLE */
  }, 8 /* PROPS */, ["modelValue"]))
}
}

})
import{createApp,nextTick}from"vue";createApp(ResearchGenerated).mount("#app");nextTick(()=>requestAnimationFrame(()=>requestAnimationFrame(()=>document.body.dataset.ready="true")));
