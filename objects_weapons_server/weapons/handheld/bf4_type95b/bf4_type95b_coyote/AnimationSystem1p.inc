animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 2/3/4
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/50

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_changeFirerate.baf
animationManager.looping 0
animationManager.length 0.38

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_deploy.baf
animationManager.length 0.85

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire1.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire2.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire3.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire4.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_reload.baf
animationManager.length 3.54167

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_run.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_sprint.baf
animationManager.length 0.634

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_tozoom.baf
animationManager.looping 0
animationManager.length 0.3

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.3

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire1.baf
animationManager.looping 0
animationManager.length 0.3

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire2.baf
animationManager.looping 0
animationManager.length 0.3

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire3.baf
animationManager.looping 0
animationManager.length 0.3

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire4.baf
animationManager.looping 0
animationManager.length 0.3

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_stand.baf


animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_run_prone.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_toprone.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_toprone_rev.baf
animationManager.length 1.2

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_changeFirerate.baf


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire.baf


animationSystem.createBundle fire1
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire1.baf


animationSystem.createBundle fire2
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire2.baf


animationSystem.createBundle fire3
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire3.baf


animationSystem.createBundle fire4
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_fire4.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_reload.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.6
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.18
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire.baf


animationSystem.createBundle zoom_fire1
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.18
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire1.baf


animationSystem.createBundle zoom_fire2
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.18
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire2.baf


animationSystem.createBundle zoom_fire3
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.18
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire3.baf


animationSystem.createBundle zoom_fire4
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.18
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_fire4.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_zoom_stand.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/bf4_type95b/bf4_type95b_coyote/animations/1p/1p_qbz_tozoom.baf


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

animationSystem.createTrigger Trigger still
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

animationSystem.createTrigger MessageTrigger changeFirerate
animationTrigger.addBundle changeFirerate
animationTrigger.message 8

animationSystem.createTrigger MessageTrigger reload
animationTrigger.addBundle reload
animationTrigger.message 2

animationSystem.createTrigger Trigger normal
animationTrigger.addChild still
animationTrigger.addChild move
animationTrigger.addChild sprint
animationTrigger.addChild fire
animationTrigger.addChild changeFirerate
animationTrigger.addChild reload

animationSystem.createTrigger SwitchMessageTrigger root
animationTrigger.addChild zoom
animationTrigger.addChild normal
animationTrigger.addBundle zoomTransition
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

