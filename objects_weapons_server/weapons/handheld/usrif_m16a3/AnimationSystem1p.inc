animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 4/3/3
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/40

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_changeFirerate.baf
animationManager.looping 0
animationManager.length 0.458333

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_deploy.baf
animationManager.looping 0
animationManager.length 1.04167

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_reload.baf
animationManager.looping 0
animationManager.length 3.33333

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_run.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_sprint.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_tozoom.baf
animationManager.looping 0
animationManager.length 0.35

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_zoom_stand.baf
animationManager.length 2.08333

beginrem

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_m16_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_m16_zoom_run.baf
animationManager.length 1.79167

animationSystem.createAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_m16_zoom_stand.baf
animationManager.length 2.08333
endrem

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_changeFirerate.baf


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.85


animationSystem.createBundle run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.9
animationBundle.fadeOutTime 0.25
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_m16_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_m16_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_m16_zoom_stand.baf

beginrem

animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/usrif_m16a3/Animations/1p/1p_ak5_tozoom.baf



animationSystem.createBundle prone_run
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/BF4_M16A4_Magnifier_on/Animations/1p/1p_m16a4BF4_pronerunleft.baf
animationBundle.addAnimation Objects/Weapons/Handheld/BF4_M16A4_Magnifier_on/Animations/1p/1p_m16a4BF4_pronerunright.baf
animationBundle.addAnimation Objects/Weapons/Handheld/BF4_M16A4_Magnifier_on/Animations/1p/1p_m16a4BF4_pronerunbackward.baf
animationBundle.addAnimation Objects/Weapons/Handheld/BF4_M16A4_Magnifier_on/Animations/1p/1p_m16a4BF4_pronerunforward.baf
animationBundle.addEvent effect:1
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

animationSystem.createTrigger MessageTrigger zoom_changeFirerate
animationTrigger.addBundle zoom_changeFirerate
animationTrigger.message 8

animationSystem.createTrigger Trigger zoom
animationTrigger.addChild zoom_still
animationTrigger.addChild zoom_move
animationTrigger.addChild zoom_fire
animationTrigger.addChild zoom_changeFirerate

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
