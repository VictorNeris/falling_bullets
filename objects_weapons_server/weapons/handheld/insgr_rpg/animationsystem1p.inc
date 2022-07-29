animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.02/0.02/0.02
animationSystem.cameraSpring.zoomDamping 2.9/2.9/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/20

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_deploy.baf
animationManager.looping 0
animationManager.length 8.5

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_fire.baf
animationManager.looping 0
animationManager.noiceFreq 3
animationManager.noiceAmplitude 0.002

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_reload.baf
animationManager.looping 0
animationManager.length 6

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_run.baf
animationManager.length 0.791667

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_stand.baf


animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_run_prone.baf
animationManager.length 0.8

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_toprone.baf
animationManager.length 1

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_toprone_rev.baf
animationManager.length 1.2

rem ========== TR zero animations ==========


animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_still_TR_zero_200.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_still_TR_zero_300.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_still_TR_zero_400.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_still_TR_zero_500.baf


animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_move_TR_zero_200.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_move_TR_zero_300.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_move_TR_zero_400.baf

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_move_TR_zero_500.baf


animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_fire_TR_zero_200.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_fire_TR_zero_300.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_fire_TR_zero_400.baf
animationManager.looping 0

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_fire_TR_zero_500.baf
animationManager.looping 0


animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_tozoom_TR_zero_200.baf
animationManager.looping 0
animationManager.length 0.95

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_tozoom_TR_zero_300.baf
animationManager.looping 0
animationManager.length 0.95

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_tozoom_TR_zero_400.baf
animationManager.looping 0
animationManager.length 0.95

animationSystem.createAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_tozoom_TR_zero_500.baf
animationManager.looping 0
animationManager.length 0.95

rem ========== TR zero bundles ==========


animationSystem.createBundle zoom_still_200
animationBundle.fadeOutTime 0.3
animationBundle.fadeInTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_still_TR_zero_200.baf


animationSystem.createBundle zoom_still_300
animationBundle.fadeOutTime 0.3
animationBundle.fadeInTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_still_TR_zero_300.baf


animationSystem.createBundle zoom_still_400
animationBundle.fadeOutTime 0.3
animationBundle.fadeInTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_still_TR_zero_400.baf


animationSystem.createBundle zoom_still_500
animationBundle.fadeOutTime 0.3
animationBundle.fadeInTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_still_TR_zero_500.baf


animationSystem.createBundle zoom_move_200
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_move_TR_zero_200.baf


animationSystem.createBundle zoom_move_300
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_move_TR_zero_300.baf


animationSystem.createBundle zoom_move_400
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_move_TR_zero_400.baf


animationSystem.createBundle zoom_move_500
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_move_TR_zero_500.baf


animationSystem.createBundle zoom_fire_200
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_fire_TR_zero_200.baf


animationSystem.createBundle zoom_fire_300
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_fire_TR_zero_300.baf


animationSystem.createBundle zoom_fire_400
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_fire_TR_zero_400.baf


animationSystem.createBundle zoom_fire_500
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_zoom_fire_TR_zero_500.baf


animationSystem.createBundle zoomTransition_200
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_tozoom_TR_zero_200.baf


animationSystem.createBundle zoomTransition_300
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_tozoom_TR_zero_300.baf


animationSystem.createBundle zoomTransition_400
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_tozoom_TR_zero_400.baf


animationSystem.createBundle zoomTransition_500
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_tozoom_TR_zero_500.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_reload.baf


animationSystem.createBundle run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_run.baf


animationSystem.createBundle sprint
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_sprint.baf


animationSystem.createBundle still
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_stand.baf



animationSystem.createBundle still_prone
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_stand.baf


animationSystem.createBundle run_prone
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_run_prone.baf


animationSystem.createBundle toProne
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_toprone.baf
animationBundle.addEvent effect:8
animationBundle.setEventStartTime effect:8 0


animationSystem.createBundle toProneReverse
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/insgr_rpg/Animations/1p/1p_insgr_rpg_toprone_rev.baf
animationBundle.addEvent effect:9
animationBundle.setEventStartTime effect:9 0

rem *** Triggers ***
animationSystem.createTrigger Trigger zoom_still
animationTrigger.addBundle zoom_still_200

animationSystem.createTrigger MovementTrigger zoom_move
animationTrigger.addBundle zoom_move_200
animationTrigger.valueHolder 1p_zoom_move

animationSystem.createTrigger MessageTrigger zoom_fire
animationTrigger.addBundle zoom_fire_200
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
animationTrigger.addBundle still_prone
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
animationTrigger.addBundle run_prone
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
animationTrigger.addBundle zoomTransition_200
animationTrigger.message 4

animationSystem.createTrigger Trigger fromProne_zoom
animationTrigger.addBundle zoom_still_200

animationSystem.createTrigger Trigger fromProne_normal
animationTrigger.addBundle toProneReverse

animationSystem.createTrigger SwitchMessageTrigger fromProne
animationTrigger.addChild fromProne_zoom
animationTrigger.addChild fromProne_normal
animationTrigger.message 4

animationSystem.createTrigger Trigger stillToProne_zoom
animationTrigger.addBundle zoom_still_200

animationSystem.createTrigger Trigger stillToProne_normal
animationTrigger.addBundle toProne

animationSystem.createTrigger SwitchMessageTrigger stillToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger forwardToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger backwardToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger leftToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4

animationSystem.createTrigger SwitchMessageTrigger rightToProne
animationTrigger.addChild stillToProne_zoom
animationTrigger.addChild stillToProne_normal
animationTrigger.message 4

animationSystem.createTrigger Trigger specialMoves
animationTrigger.addChild fromProne
animationTrigger.addChild stillToProne
animationTrigger.addChild forwardToProne
animationTrigger.addChild backwardToProne
animationTrigger.addChild leftToProne
animationTrigger.addChild rightToProne

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup
animationTrigger.addChild specialMoves

