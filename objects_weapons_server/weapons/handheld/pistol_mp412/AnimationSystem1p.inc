animationSystem.cameraSpring.use 1
animationSystem.cameraSpring.amplitude 0.03/0.02/0.03
animationSystem.cameraSpring.zoomDamping 4/2.5/1
animationSystem.cameraSpring.stiffness 10/10/10
animationSystem.cameraSpring.move 2/1/1
animationSystem.cameraSpring.look 1/1
animationSystem.cameraSpring.fire 0/0/90

rem *** Animations ***

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_deploy.baf
animationManager.looping 0
animationManager.length 0.75

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_fire.baf
animationManager.looping 0
animationManager.length 0.27

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_reload.baf
animationManager.looping 0
animationManager.length 4.5

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_run.baf
animationManager.length 0.61

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_sprint.baf

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_stand.baf

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_zoom_fire.baf
animationManager.looping 0
animationManager.length 0.27

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_zoom_run.baf
animationManager.length 1.8

animationSystem.createAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_zoom_stand.baf

rem *** Bundles ***

animationSystem.createBundle deploy
animationBundle.isLooping 0
animationBundle.fadeInTime 0.001
animationBundle.fadeOutTime 0.4
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_deploy.baf


animationSystem.createBundle fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_fire.baf


animationSystem.createBundle reload
animationBundle.isLooping 0
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.3
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_reload.baf
animationBundle.addEvent effect:0
animationBundle.setEventStartTime effect:0 0.7


animationSystem.createBundle run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_run.baf


animationSystem.createBundle sprint
animationBundle.fadeInTime 0.3
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_sprint.baf


animationSystem.createBundle still
animationBundle.fadeInTime 0.15
animationBundle.fadeOutTime 0.15
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_stand.baf


animationSystem.createBundle zoom_fire
animationBundle.isLooping 0
animationBundle.abruptPlayback 1
animationBundle.fadeInTime 0.001
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_zoom_fire.baf


animationSystem.createBundle zoom_run
animationBundle.fadeOutTime 0.2
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_zoom_run.baf


animationSystem.createBundle zoom_still
animationBundle.addAnimation Objects/Weapons/Handheld/pistol_mp412/Animations/1p/1p_mk6_zoom_stand.baf


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
animationTrigger.fadeInTime 0.2
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
animationTrigger.message 4

animationSystem.createTrigger Trigger startup
animationTrigger.addBundle deploy

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root
animationTrigger.addChild startup

