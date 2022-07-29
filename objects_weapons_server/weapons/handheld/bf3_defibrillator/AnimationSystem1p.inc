animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.045/0.045/0.045
animationSystem.cameraSpring.zoomDamping 2.5/2.5/0
animationSystem.cameraSpring.stiffness 50/50/50
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_deploy.baf
animationManager.looping 0
animationManager.length 0.833333

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_fire.baf
animationManager.looping 0
animationManager.length 0.958333

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/animations/1p/1p_defibrillator_fire_new.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_Idle2.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/animations/1p/1p_defibrillator_reload_new.baf
animationManager.looping 0
animationManager.length 1.5

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/animations/1p/1p_defibrillator_run_new2.baf
animationManager.looping 0
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_sprint.baf
animationManager.looping 0
animationManager.length 3.16667

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_stand.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/bf3_defibrillator/animations/1p/1p_defibrillator_stand_new.baf
animationManager.length 2.04167

rem *** Bundles ***

animationSystem.createBundle changeFirerate
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001


animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.5
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/animations/1p/1p_defibrillator_fire_new.baf


animationSystem.createBundle idle1
animationBundle.isLooping 0
animationBundle.fadeInTime 0.1
animationBundle.fadeOutTime 0.2


animationSystem.createBundle idle2
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_Idle2.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/animations/1p/1p_defibrillator_reload_new.baf


animationSystem.createBundle run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/animations/1p/1p_defibrillator_run_new2.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_sprint.baf


animationSystem.createBundle still
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/animations/1p/1p_defibrillator_stand_new.baf


animationSystem.createBundle zoom_changeFirerate
animationBundle.isLooping 0


animationSystem.createBundle zoom_fire
animationBundle.fadeInTime 0.001


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2


animationSystem.createBundle zoom_stand
animationBundle.isLooping 0
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_stand.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/bf3_defibrillator/Animations/1p/1p_defibrillator_fire.baf


rem *** Triggers ***
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
animationTrigger.addChild normal
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

