animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.05
animationSystem.cameraSpring.zoomDamping 3/3/0.5
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/10

rem *** Animations ***
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_DEPLOY.baf
animationManager.length 1.9
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_FIRE.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.583333
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_mg3_idle.baf
animationManager.length 2.70833
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_reload.baf
animationManager.looping 0
animationManager.length 8.15
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_RUN.baf
animationManager.length 0.625
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_mg3_run_prone.baf
animationManager.length 0.791667
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_sprint.baf
animationManager.length 0.8
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_stand.baf
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_mg3_toprone.baf
animationManager.length 1
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_mg3_toprone_rev.baf
animationManager.looping 0
animationManager.length 1
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_tozoom.baf
animationManager.looping 0
animationManager.length 0.95
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.583333
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_zoom_run.baf
animationManager.length 1.79167
animationSystem.createAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_zoom_stand.baf

rem *** Bundles ***
animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 1.4
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_DEPLOY.baf

animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_FIRE.baf

animationSystem.createBundle Idle
animationBundle.isLooping 0
animationBundle.fadeInTime 0.6
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_mg3_idle.baf

animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.45
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_reload.baf

animationSystem.createBundle run
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_RUN.baf

animationSystem.createBundle run_prone
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_mg3_run_prone.baf

animationSystem.createBundle sprint
animationBundle.fadeInTime 1.0
animationBundle.fadeOutTime 0.55
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_sprint.baf

animationSystem.createBundle still
animationBundle.fadeInTime 0.5
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_stand.baf

animationSystem.createBundle toProne
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_mg3_toprone.baf

animationSystem.createBundle toProneReverse
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_mg3_toprone_rev.baf

animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_zoom_fire.baf

animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_zoom_run.baf

animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_zoom_stand.baf

animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/play4free_mg3/Animations/1p/1p_MG3_tozoom.baf


rem *** Triggers ***
animationSystem.createTrigger Trigger zoom_still
animationTrigger.addBundle zoom_still

animationSystem.createTrigger MovementTrigger zoom_move
animationTrigger.addBundle zoom_run
animationTrigger.valueHolder 1p_zoom_move

animationSystem.createTrigger MessageTrigger zoom_fire
animationTrigger.addBundle zoom_fire
animationTrigger.message 1

animationSystem.createTrigger Trigger zoom
animationTrigger.addChild zoom_still
animationTrigger.addChild zoom_move
animationTrigger.addChild zoom_fire

animationSystem.createTrigger IdleTrigger Idle
animationTrigger.addBundle Idle
animationTrigger.idleTime 5/10

animationSystem.createTrigger Trigger still
animationTrigger.addChild Idle
animationTrigger.addBundle still

animationSystem.createTrigger MovementTrigger move
animationTrigger.addBundle run
animationTrigger.valueHolder 1p_move

animationSystem.createTrigger MovementTrigger sprint
animationTrigger.addBundle sprint
animationTrigger.valueHolder 1p_sprint

animationSystem.createTrigger MessageTrigger fire
animationTrigger.addBundle fire
animationTrigger.message 1

animationSystem.createTrigger MessageTrigger reload
animationTrigger.addBundle reload
animationTrigger.message 2

animationSystem.createTrigger Trigger normal
animationTrigger.fadeInTime 0.2
animationTrigger.addChild still
animationTrigger.addChild move
animationTrigger.addChild sprint
animationTrigger.addChild fire
animationTrigger.addChild reload

animationSystem.createTrigger SwitchMessageTrigger root
animationTrigger.addChild zoom
animationTrigger.addChild normal
animationTrigger.addBundle zoomTransition
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
rem animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup


