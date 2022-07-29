animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.045/0.045/0.045
animationSystem.cameraSpring.zoomDamping 2.5/2.5/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 3/3/3
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

rem *** Bundles ***
animationSystem.createBundle swim_still
animationBundle.length 2.0

animationSystem.createBundle swim_backward
animationBundle.length 2.0

animationSystem.createBundle swim_forward
animationBundle.length 2.0

animationSystem.createBundle swim_sprint
animationBundle.length 1.3


rem *** Triggers ***
animationSystem.createTrigger Trigger stand

animationSystem.createTrigger Trigger crouch

animationSystem.createTrigger Trigger prone

animationSystem.createTrigger MovementTrigger swim_still
animationTrigger.addBundle swim_still

animationSystem.createTrigger ForwardTrigger swim_forward
animationTrigger.addBundle swim_forward
animationTrigger.valueHolder 3p_swimForward

animationSystem.createTrigger ForwardTrigger swim_backward
animationTrigger.addBundle swim_backward
animationTrigger.valueHolder 3p_swimBackward

animationSystem.createTrigger ForwardTrigger swim_sprint
animationTrigger.addBundle swim_sprint
animationTrigger.valueHolder 3p_swimSprint

animationSystem.createTrigger Trigger swim
animationTrigger.addChild swim_still
animationTrigger.addChild swim_forward
animationTrigger.addChild swim_backward
animationTrigger.addChild swim_sprint

animationSystem.createTrigger PoseTrigger pose
animationTrigger.addChild stand
animationTrigger.addChild crouch
animationTrigger.addChild prone
animationTrigger.addChild swim

animationSystem.createTrigger Trigger root
animationTrigger.addChild pose

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
