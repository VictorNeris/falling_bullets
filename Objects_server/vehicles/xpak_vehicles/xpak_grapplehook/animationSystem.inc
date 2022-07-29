
rem *** Animations ***
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_climb2.baf
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_lower2.baf
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_climb2_pause.baf
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_roofup2.baf
animationSystem.createAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_roofdown.baf

rem *** Bundles ***
animationSystem.createBundle climbup
animationBundle.fadeInTime 0.0
animationBundle.fadeOutTime 0.0
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_climb2.baf

animationSystem.createBundle climbdown
animationBundle.fadeInTime 0.0
animationBundle.fadeOutTime 0.0
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_lower2.baf

animationSystem.createBundle hang
animationBundle.fadeInTime 0.0
animationBundle.fadeOutTime 0.0
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_climb2_pause.baf

animationSystem.createBundle climbontop
animationBundle.fadeInTime 0.0
animationBundle.fadeOutTime 0.0
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_roofup2.baf

animationSystem.createBundle climbofftop
animationBundle.fadeInTime 0.0
animationBundle.fadeOutTime 0.0
animationBundle.addAnimation Objects/Vehicles/xpak_vehicles/xpak_grapplehook/3P/grapplehook_roofdown.baf


animationSystem.createTrigger MessageTrigger ClimbUp
animationTrigger.addBundle climbup
animationTrigger.message 1

animationSystem.createTrigger MessageTrigger ClimbDown
animationTrigger.addBundle climbdown
animationTrigger.message 2

animationSystem.createTrigger MessageTrigger Hang
animationTrigger.addBundle hang
animationTrigger.message 4

animationSystem.createTrigger MessageTrigger ClimbOnTop
animationTrigger.addBundle climbontop
animationTrigger.message 8

animationSystem.createTrigger MessageTrigger ClimbOffTop
animationTrigger.addBundle climbofftop
animationTrigger.message 16

animationSystem.createTrigger Trigger root
animationTrigger.addChild ClimbUp
animationTrigger.addChild ClimbDown
animationTrigger.addChild Hang
animationTrigger.addChild ClimbOnTop
animationTrigger.addChild ClimbOffTop

animationSystem.createTrigger Trigger completeTree
animationTrigger.addChild root