animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.015/0.015/0.015
animationSystem.cameraSpring.zoomDamping 2.5/2.5/0
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/2/2
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/150

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_deploy.baf
animationManager.length 1.04167

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_fire.baf
animationManager.looping 0
animationManager.length 1.33333

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_fire_pinremove.baf
animationManager.length 1.04167

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_fire_throw.baf
animationManager.looping 0
animationManager.length 0.416667

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_run.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_run_load.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_sprint.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_sprint_load.baf
animationManager.length 0.666667

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_stand_load.baf

animationSystem.createAnimation Objects/Weapons/Handheld/ushgr_m67/Animations/1p/1p_m67_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.fadeOutTime 0
animationBundle.playForever 1
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_fire.baf


animationSystem.createBundle normal_run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_run.baf


animationSystem.createBundle normal_sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_sprint.baf


animationSystem.createBundle normal_still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/Animations/1p/1p_m67_stand.baf


animationSystem.createBundle pinremove
animationBundle.isLooping 0
animationBundle.fadeInTime 0
animationBundle.fadeOutTime 0.1
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_fire_pinremove.baf


animationSystem.createBundle uncocked_fire
animationBundle.isLooping 0
animationBundle.fadeOutTime 0
animationBundle.playForever 1
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_fire_throw.baf


animationSystem.createBundle uncocked_run
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_run_load.baf


animationSystem.createBundle uncocked_sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_sprint_load.baf


animationSystem.createBundle uncocked_still
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/animations/1p/1p_67_stand_load.baf


animationSystem.createBundle idle1
animationBundle.isLooping 0
animationBundle.fadeInTime 0.6
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/Animations/1p/1p_m67_idle1.baf


animationSystem.createBundle idle2
animationBundle.isLooping 0
animationBundle.fadeInTime 0.6
animationBundle.fadeOutTime 0.6
animationBundle.addAnimation Objects/Weapons/Handheld/ushgr_m67/Animations/1p/1p_m67_idle2.baf


rem *** Triggers ***
animationSystem.createTrigger IdleTrigger idle
animationTrigger.addBundle idle1
animationTrigger.addBundle idle2
animationTrigger.idleTime 5/10

animationSystem.createTrigger Trigger normal_still
animationTrigger.addChild idle
animationTrigger.addBundle normal_still

animationSystem.createTrigger MovementTrigger normal_move
animationTrigger.addBundle normal_run
animationTrigger.valueHolder 1p_move

animationSystem.createTrigger MovementTrigger normal_sprint
animationTrigger.addBundle normal_sprint
animationTrigger.valueHolder 1p_sprint

animationSystem.createTrigger MessageTrigger fire
animationTrigger.addBundle fire
animationTrigger.message 1

animationSystem.createTrigger MessageTrigger reload
animationTrigger.addBundle deploy
animationTrigger.message 2

animationSystem.createTrigger Trigger normal
animationTrigger.addChild normal_still
animationTrigger.addChild normal_move
animationTrigger.addChild normal_sprint
animationTrigger.addChild fire
animationTrigger.addChild reload

animationSystem.createTrigger Trigger uncocked_still
animationTrigger.addBundle uncocked_still

animationSystem.createTrigger MovementTrigger uncocked_move
animationTrigger.addBundle uncocked_run
animationTrigger.valueHolder 1p_move

animationSystem.createTrigger MovementTrigger uncocked_sprint
animationTrigger.addBundle uncocked_sprint
animationTrigger.valueHolder 1p_sprint

animationSystem.createTrigger MessageTrigger uncocked_pinremove
animationTrigger.addBundle pinremove
animationTrigger.message 16

animationSystem.createTrigger MessageTrigger uncocked_fire
animationTrigger.addBundle uncocked_fire
animationTrigger.message 1

animationSystem.createTrigger MessageTrigger uncocked_fireShort
animationTrigger.addBundle uncocked_fireShort
animationTrigger.message 4

animationSystem.createTrigger Trigger uncocked
animationTrigger.addChild uncocked_still
animationTrigger.addChild uncocked_move
animationTrigger.addChild uncocked_sprint
animationTrigger.addChild uncocked_pinremove
animationTrigger.addChild uncocked_fire
animationTrigger.addChild uncocked_fireShort

animationSystem.createTrigger SwitchMessageTrigger root
animationTrigger.addChild normal
animationTrigger.addChild uncocked
animationTrigger.message 8

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

