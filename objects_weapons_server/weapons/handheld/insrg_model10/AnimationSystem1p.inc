animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 2/3/4
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/50

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_deploy.baf
animationManager.looping 0
animationManager.length 0.55

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire1.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire2.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire3.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire4.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_reload.baf
animationManager.looping 0
animationManager.length 4.7

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_run.baf
animationManager.length 0.64

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_tozoom.baf
animationManager.looping 0
animationManager.length 0.08

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire1.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire2.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire3.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire4.baf
animationManager.looping 0
animationManager.length 0.583333

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_run.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_stand.baf


animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_run_prone.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_toprone.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_toprone_rev.baf
animationManager.length 1.2

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0.00
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire.baf


animationSystem.createBundle fire1
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire1.baf


animationSystem.createBundle fire2
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire2.baf


animationSystem.createBundle fire3
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire3.baf


animationSystem.createBundle fire4
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.01
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_fire4.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.2
animationBundle.fadeOutTime 0.35
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_reload.baf


animationSystem.createBundle run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.fadeInTime 0.01
animationBundle.abruptPlayback 1
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire.baf


animationSystem.createBundle zoom_fire1
animationBundle.isLooping 0
animationBundle.fadeInTime 0.01
animationBundle.abruptPlayback 1
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire1.baf


animationSystem.createBundle zoom_fire2
animationBundle.isLooping 0
animationBundle.fadeInTime 0.01
animationBundle.abruptPlayback 1
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire2.baf


animationSystem.createBundle zoom_fire3
animationBundle.isLooping 0
animationBundle.fadeInTime 0.01
animationBundle.abruptPlayback 1
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire3.baf


animationSystem.createBundle zoom_fire4
animationBundle.isLooping 0
animationBundle.fadeInTime 0.01
animationBundle.abruptPlayback 1
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_fire4.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_zoom_stand.baf


animationSystem.createBundle zoomTransition
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_tozoom.baf



animationSystem.createBundle run_prone
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_run_prone.baf


animationSystem.createBundle toProne
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_toprone.baf
animationBundle.addEvent effect:8
animationBundle.setEventStartTime effect:8 0


animationSystem.createBundle toProneReverse
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insrg_model10/Animations/1p/1p_sw40_toprone_rev.baf
animationBundle.addEvent effect:9
animationBundle.setEventStartTime effect:9 0

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

animationSystem.createTrigger Trigger still_stand_t
animationTrigger.addBundle still
animationTrigger.addChild idle

animationSystem.createTrigger Trigger still_crouch_t
animationTrigger.addBundle still
animationTrigger.addChild idle

animationSystem.createTrigger Trigger still_prone_t
animationTrigger.addBundle still
animationTrigger.addChild idle

animationSystem.createTrigger PoseTrigger still
animationTrigger.addChild still_stand_t
animationTrigger.addChild still_crouch_t
animationTrigger.addChild still_prone_t
animationTrigger.addChild still_prone_t

animationSystem.createTrigger MovementTrigger move_stand_t
animationTrigger.addBundle run
animationTrigger.valueHolder 1p_move

animationSystem.createTrigger MovementTrigger move_crouch_t
animationTrigger.addBundle run
animationTrigger.valueHolder 1p_move

animationSystem.createTrigger MovementTrigger move_prone_t
animationTrigger.addBundle run
animationTrigger.valueHolder 1p_move

animationSystem.createTrigger PoseTrigger move
animationTrigger.addChild move_stand_t
animationTrigger.addChild move_crouch_t
animationTrigger.addChild move_prone_t
animationTrigger.addChild move_prone_t

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
rem animationTrigger.addChild specialMoves

