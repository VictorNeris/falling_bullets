
rem *** Animations ***
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_ailraider/3p/xpak_ailraider_driverB.baf
animationManager.looping 0
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_ailraider/3p/xpak_ailraider_driverF.baf
animationManager.looping 0

rem *** Bundles ***
animationSystem.createBundle LeanLR
animationBundle.isLooping 0
animationBundle.fadeInTime 0.25
animationBundle.fadeOutTime 0.25
animationBundle.useSpeedAsTime 1
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_ailraider/3p/xpak_ailraider_driverF.baf
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_ailraider/3p/xpak_ailraider_driverB.baf


rem *** Triggers ***
animationSystem.createTrigger LookAroundTrigger root
animationTrigger.addBundle LeanLR
animationTrigger.valueHolder 3p_turnRight

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root

