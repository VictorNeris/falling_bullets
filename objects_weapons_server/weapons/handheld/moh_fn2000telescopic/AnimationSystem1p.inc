animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.02/0.02/0.02
animationSystem.cameraSpring.zoomDamping 10/10/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/30

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_chnagefirerate.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_deploy.baf
animationManager.looping 0
animationManager.length 0.833333

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_reload.baf
animationManager.length 3.33333

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_run.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_sprint.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_tozoom.baf
animationManager.looping 0
animationManager.length 0.22

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_zoom_fire_scope.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_zoom_run_scope.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_zoom_stand_scope.baf

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_chnagefirerate.baf


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.25
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.55


animationSystem.createBundle run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.7
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_zoom_fire_scope.baf


animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_zoom_run_scope.baf


animationSystem.createBundle zoom_still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_zoom_stand_scope.baf

beginrem

animationSystem.createBundle zoomTransitions
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/moh_fn2000telescopic/Animations/1p/1p_f2000_tozoom.baf
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
animationTrigger.addBundle zoomTransitions
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

