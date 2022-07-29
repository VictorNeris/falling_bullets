
rem *** Animations ***
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_civ2/3p/xpak_civ2GunnerDown.baf
animationManager.looping 0
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_civ2/3p/xpak_civ2GunnerUp.baf
animationManager.looping 0

rem *** Bundles ***
animationSystem.createBundle LeanLR
animationBundle.isLooping 0
animationBundle.playBackward 1
animationBundle.fadeInTime 0.25
animationBundle.fadeOutTime 0.25
animationBundle.useSpeedAsTime 1
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_civ2/3p/xpak_civ2GunnerUp.baf
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_civ2/3p/xpak_civ2GunnerDown.baf


rem *** Triggers ***
animationSystem.createTrigger LookAroundTrigger root
animationTrigger.addBundle LeanLR
animationTrigger.valueHolder 3p_turnRight

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root

