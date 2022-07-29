
rem *** Animations ***
animationSystem.createAnimation Objects/Vehicles/Air/chthe_z8/animations/3p/3p_chthe_z8_pilot_static.baf
animationManager.looping 1
animationSystem.createAnimation Objects/Vehicles/Air/chthe_z8/animations/3p/3p_chthe_z8_pilot_die.baf
animationManager.looping 1

rem *** Bundles ***
animationSystem.createBundle still
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.isLooping 1
animationBundle.useSpeedAsTime 1
animationBundle.addAnimation Objects/Vehicles/Air/chthe_z8/animations/3p/3p_chthe_z8_pilot_static.baf

animationSystem.createBundle die
animationBundle.fadeInTime 0.4
animationBundle.isLooping 0
animationBundle.playForever 1
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Vehicles/Air/chthe_z8/animations/3p/3p_chthe_z8_pilot_die.baf

rem *** Triggers ***
animationSystem.createTrigger Trigger root
animationTrigger.addBundle still

animationSystem.createTrigger Trigger die
animationTrigger.addBundle die

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild die

