
rem *** Animations ***
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_zipline/3p/xpak_zipline_hang.baf
animationManager.looping 0
animationManager.fadeInTime 0.5

rem *** Bundles ***
animationSystem.createBundle LeanLR
animationBundle.isLooping 0
animationBundle.playBackward 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.useSpeedAsTime 1
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_zipline/3p/xpak_zipline_hang.baf
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_zipline/3p/xpak_zipline_hang.baf


rem *** Triggers ***
animationSystem.createTrigger LookAroundTrigger root
animationTrigger.addBundle LeanLR
animationTrigger.valueHolder 3p_turnRight

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root

