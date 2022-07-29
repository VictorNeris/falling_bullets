animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.02/0.02/0.05
animationSystem.cameraSpring.zoomDamping 2/2/1
animationSystem.cameraSpring.stiffness 2/2/2
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/10

rem *** Animations ***
animationSystem.createAnimation Objects/Weapons/handheld/uslmg_m249saw/animations/1p/1p_m249saw_deploy.baf
animationManager.looping 0
animationManager.length 1.54167
animationSystem.createAnimation Objects/Weapons/handheld/uslmg_m249saw/animations/1p/1p_m249saw_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002
animationManager.length 0.583333
animationSystem.createAnimation Objects/Weapons/handheld/uslmg_m249saw/animations/1p/1p_qjy88_reload.baf
animationManager.length 7.3
animationSystem.createAnimation Objects/Weapons/handheld/uslmg_m249saw/animations/1p/1p_m249saw_run.baf
animationManager.length 0.666667
animationSystem.createAnimation Objects/Weapons/handheld/uslmg_m249saw/animations/1p/1p_m249saw_sprint.baf
animationManager.length 0.666667
animationSystem.createAnimation Objects/Weapons/handheld/uslmg_m249saw/animations/1p/1p_m249saw_stand.baf
animationSystem.createAnimation Objects/Weapons/Handheld/MG_Saw_Elcan/Animations/1p/1p_Elcan_tozoom.baf
animationManager.looping 0
animationManager.length 0.8
animationSystem.createAnimation Objects/Weapons/Handheld/MG_Saw_Elcan/Animations/1p/1p_Elcan_zoom_fire.baf
animationManager.looping 0
animationSystem.createAnimation Objects/Weapons/Handheld/MG_Saw_Elcan/Animations/1p/1p_Elcan_zoom_run.baf
animationManager.length 1.83333
animationSystem.createAnimation Objects/Weapons/Handheld/MG_Saw_Elcan/Animations/1p/1p_Elcan_zoom_stand.baf

rem *** Bundles ***
animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/uslmg_m249saw/Animations/1p/1p_m249saw_deploy.baf

animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/USLMG_M249SAW/Animations/1p/1p_m249saw_fire.baf

animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.25
animationBundle.fadeOutTime 0.85
animationBundle.addAnimation Objects/Weapons/Handheld/USLMG_M249SAW/Animations/1p/1p_qjy88_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 2.85

animationSystem.createBundle run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/USLMG_M249SAW/Animations/1p/1p_m249saw_run.baf

animationSystem.createBundle sprint
animationBundle.fadeInTime 0.9
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/USLMG_M249SAW/Animations/1p/1p_m249saw_sprint.baf

animationSystem.createBundle still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/USLMG_M249SAW/Animations/1p/1p_m249saw_stand.baf

animationSystem.createBundle zoom_changeFirerate
animationBundle.isLooping 0

animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/MG_Saw_Elcan/Animations/1p/1p_Elcan_zoom_fire.baf

animationSystem.createBundle zoom_run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/MG_Saw_Elcan/Animations/1p/1p_Elcan_zoom_run.baf

animationSystem.createBundle zoom_still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/MG_Saw_Elcan/Animations/1p/1p_Elcan_zoom_stand.baf

beginrem
animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/MG_Saw_Elcan/Animations/1p/1p_Elcan_tozoom.baf
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
animationTrigger.addBundle zoomTransition
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
rem animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

