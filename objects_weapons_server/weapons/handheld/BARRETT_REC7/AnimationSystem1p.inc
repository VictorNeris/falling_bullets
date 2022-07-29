animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.02/0.02/0.02
animationSystem.cameraSpring.zoomDamping 2.9/2.9/1.0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/50

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_changeFirerate.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_deploy.baf
animationManager.looping 0
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.4

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_reload.baf
animationManager.looping 0
animationManager.length 3

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_run.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_stand.baf


animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_changefirerate.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_deploy.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.833333

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_reload.baf
animationManager.length 3.33333

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_run.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_sprint.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_tozoom.baf
animationManager.looping 0
animationManager.length 0.25

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_zoom_run.baf

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_zoom_stand.baf


animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_hk416_zoomfire.baf
animationManager.looping 0
animationManager.length 0.2

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_hk416_zoomrun.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_hk416_zoomstand.baf

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.0
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_changeFirerate.baf


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.58333
animationBundle.addAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_reload.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.85
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m4moh_reflex/Animations/1p/1p_m4a1_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
rem animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_hk416_zoomfire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_hk416_zoomrun.baf


animationSystem.createBundle zoom_still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_hk416_zoomstand.baf

beginrem

animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/BARRETT_REC7/Animations/1p/1p_rec7_tozoom.baf
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
animationTrigger.addBundle zoomTransition
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

