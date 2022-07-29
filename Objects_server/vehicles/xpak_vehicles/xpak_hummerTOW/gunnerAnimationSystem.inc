
rem *** Animations ***
animationSystem.createAnimation Objects/Vehicles/Land/USJEP_HMMWV/Animations/3p/3p_usjep_hmmwv_gunner_sit.baf
animationManager.looping 0
animationSystem.createAnimation Objects/Vehicles/Land/USJEP_HMMWV/Animations/3p/3p_usjep_hmmwv_gunner_stand.baf
animationManager.looping 0

rem *** Bundles ***
animationSystem.createBundle lookAround
animationBundle.isLooping 0
animationBundle.playBackward 1
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.useSpeedAsTime 1
animationBundle.addAnimation Objects/Vehicles/Land/USJEP_HMMWV/Animations/3p/3p_usjep_hmmwv_gunner_stand.baf
animationBundle.addAnimation Objects/Vehicles/Land/USJEP_HMMWV/Animations/3p/3p_usjep_hmmwv_gunner_sit.baf


rem *** Triggers ***
animationSystem.createTrigger LookAroundTrigger root
animationTrigger.addBundle lookAround
animationTrigger.valueHolder 3p_turnRight

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root

