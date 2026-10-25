import {setup,createActor} from './tool/node_modules/xstate';
const machine=setup({types:{context:{} as {value:string},events:{} as {type:'SET';value:string}}}).createMachine({context:{value:'alpha'},initial:'ready',states:{ready:{}}});
const actor=createActor(machine);actor.send({type:'SET',value:'beta'});
