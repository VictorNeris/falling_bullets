
rem *** Animations ***

animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_atv/3p/atv_turnback.baf
animationManager.looping 0
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_atv/3p/atv_turnforward.baf
animationManager.looping 0

rem *** Bundles ***

animationSystem.createBundle LeanLR
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.useSpeedAsTime 1
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_atv/3p/atv_turnforward.baf
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_atv/3p/atv_turnback.baf


rem *** Triggers ***

animationSystem.createTrigger LookAroundTrigger root
animationTrigger.addBundle LeanLR
animationTrigger.valueHolder 3p_turnRight


animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root