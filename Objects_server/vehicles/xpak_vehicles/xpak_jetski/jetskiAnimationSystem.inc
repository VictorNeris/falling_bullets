
rem *** Animations ***
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_jetski/3P/sit.baf
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_jetski/3P/stand.baf

rem *** Bundles ***
animationSystem.createBundle LeanLR
animationBundle.isLooping 0
animationBundle.useSpeedAsTime 1
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_jetski/3P/stand.baf
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_jetski/3P/sit.baf


rem *** Triggers ***
animationSystem.createTrigger LookAroundTrigger root
animationTrigger.addBundle LeanLR
animationTrigger.valueHolder 3p_turnRight

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root

