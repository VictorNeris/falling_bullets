
rem *** Animations ***
animationSystem.createAnimation Objects/Common/Flags/Animations/flag_idle_wall.baf

rem *** Bundles ***
animationSystem.createBundle flag_idle_wall
animationBundle.fadeInTime 5
animationBundle.fadeOutTime 5
animationBundle.addAnimation Objects/Common/Flags/Animations/flag_idle_wall.baf

rem *** Triggers ***
animationSystem.createTrigger Trigger root
animationTrigger.addBundle flag_idle_wall



