
rem *** Animations ***
animationSystem.createAnimation Objects/Common/Flags/Animations/flag_idle.baf

rem *** Bundles ***
animationSystem.createBundle flag_idle
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Common/Flags/Animations/flag_idle.baf

rem *** Triggers ***
animationSystem.createTrigger Trigger root
animationTrigger.addBundle flag_idle



