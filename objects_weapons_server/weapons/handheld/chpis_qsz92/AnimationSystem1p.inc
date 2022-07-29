animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.035/0.01/0.035
animationSystem.cameraSpring.zoomDamping 2.5/2.5/1.5
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/10

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_deploy.baf
animationManager.length 0.833333

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_fire.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_reload.baf
animationManager.looping 0
animationManager.length 2.54167

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_run.baf
animationManager.looping 0
animationManager.length 0.625

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_sprint.baf
animationManager.looping 0
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_tozoom.baf
animationManager.looping 0
animationManager.length 0.08

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire1.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire2.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire3.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire4.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_stand.baf


animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_run_prone.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_toprone.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_toprone_rev.baf
animationManager.length 1.2

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_reload.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.15
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.4
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.15
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire.baf


animationSystem.createBundle zoom_fire1
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire1.baf


animationSystem.createBundle zoom_fire2
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire2.baf


animationSystem.createBundle zoom_fire3
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire3.baf


animationSystem.createBundle zoom_fire4
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_fire4.baf


animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.15
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.fadeInTime 0.15
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_zoom_stand.baf


animationSystem.createBundle Zoom_Transition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/chpis_qsz92/Animations/1p/1p_qsz92_tozoom.baf

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