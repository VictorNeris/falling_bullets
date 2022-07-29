
rem *** Animations ***
animationSystem.createAnimation Objects/Weapons/Handheld/nightvisiongoggles/Animations/3p/3p_nightvisiongoggles_crouchdeploy.baf
animationManager.looping 0
animationSystem.createAnimation Objects/Weapons/HandHeld/nightvisiongoggles/Animations/3p/3p_nightvisiongoggles_proneDeploy.baf
animationManager.looping 0
animationSystem.createAnimation Objects/Weapons/HandHeld/nightvisiongoggles/Animations/3p/3p_nightvisiongoggles_standDeploy.baf
animationManager.looping 0
animationManager.ignoreMotherOrientation 12

rem *** Bundles ***
animationSystem.createBundle crouchDeploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/nightvisiongoggles/Animations/3p/3p_nightvisiongoggles_crouchdeploy.baf

animationSystem.createBundle proneDeploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.addAnimation Objects/Weapons/HandHeld/nightvisiongoggles/Animations/3p/3p_nightvisiongoggles_proneDeploy.baf

animationSystem.createBundle standDeploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.addAnimation Objects/Weapons/HandHeld/nightvisiongoggles/Animations/3p/3p_nightvisiongoggles_standDeploy.baf



rem *** Triggers ***
animationSystem.createTrigger Trigger standDeploy
animationTrigger.addBundle standDeploy

animationSystem.createTrigger Trigger crouchDeploy
animationTrigger.addBundle crouchDeploy

animationSystem.createTrigger Trigger proneDeploy
animationTrigger.addBundle proneDeploy

animationSystem.createTrigger PoseTrigger startup
animationTrigger.addChild standDeploy
animationTrigger.addChild crouchDeploy
animationTrigger.addChild proneDeploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild startup

