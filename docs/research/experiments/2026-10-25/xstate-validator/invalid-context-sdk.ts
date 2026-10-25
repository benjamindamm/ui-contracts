import {setup} from './tool/node_modules/xstate';
setup({types:{context:{} as {value:string},events:{} as {type:'SET';value:string}}}).createMachine({context:{value:42},initial:'ready',states:{ready:{}}});
