animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.05
animationSystem.cameraSpring.zoomDamping 8/8/1
animationSystem.cameraSpring.stiffness 2/2/2
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/15

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_deploy.baf
animationManager.length 1.25

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_AA12_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_pronebackward.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_proneforward.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_proneleft.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_proneright.baf
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_reload.baf
animationManager.looping 0
animationManager.length 4.04167

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_AA12_run.baf
animationManager.length 0.625

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_run_toprone.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_AA12_sprint.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_AA12_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_toprone.baf
animationManager.length 1.04167

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_toprone_rev.baf
animationManager.length 1.20833

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_tozoom.baf
animationManager.looping 0
animationManager.length 0.6

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_zoom_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_zoom_toprone.baf
animationManager.length 1.3

animationSystem.createAnimation Objects/Weapons/Handheld/mohw_aa12/animations/1p/1p_aa12_zoom_toprone_rev.baf
animationManager.length 1.2

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 1.0
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_deploy.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_reload.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_AA12_fire.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.25
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_AA12_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.9
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_AA12_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.25
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_AA12_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.25
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.fadeInTime 0.25
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_zoom_stand.baf

beginrem

animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/mohw_aa12/Animations/1p/1p_aa12_tozoom.baf
endrem

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

animationSystem.createTrigger RandomTrigger rnd_idle
animationTrigger.addBundle idle1
animationTrigger.addBundle idle2

animationSystem.createTrigger IdleTrigger idle
animationTrigger.addChild rnd_idle
animationTrigger.idleTime 5/15

animationSystem.createTrigger Trigger still
animationTrigger.addChild idle
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
animationTrigger.addBundle ZoomTransition
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup
