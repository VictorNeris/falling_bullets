rem ///////////////////////////////////////////////////////////////////////////
rem 
rem			Adjust Ragdoll Gravity and Speed
rem
rem ///////////////////////////////////////////////////////////////////////////

vars.set ragdoll_slowMotion 0.850
vars.set ragdoll_gravityOverTime 0.1
Vars.Set ragdoll_sleep 2.00000
Vars.Set ragdoll-max-inherit-speed 2.000000
Vars.Set ragdoll_expRotateForce 0.50000

rem ///////////////////////////////////////////////////////////////////////////
rem 
rem			Polar angle constraints
rem
rem ///////////////////////////////////////////////////////////////////////////

ragDoll.addAngularConstraint 31 6 7 120.0
ragDoll.addAngularConstraint 15 1 2 120.0

ragDoll.addAngularConstraint 1 2 4 0.0
ragDoll.addAngularConstraint 1 2 4 0.0
ragDoll.addAngularConstraint 6 7 9 0.0
ragDoll.addAngularConstraint 6 7 9 0.0

ragDoll.addAngularConstraint 1 6 7 70.0
ragDoll.addAngularConstraint 6 1 2 100.0

ragDoll.addAngularConstraint 15 16 19 220.0
ragDoll.addAngularConstraint 15 16 19 100.0
ragDoll.addAngularConstraint 31 32 34 220.0
ragDoll.addAngularConstraint 31 32 34 100.0

ragDoll.addAngularConstraint 6 31 32 30.0
ragDoll.addAngularConstraint 1 15 16 30.0

ragDoll.addAngularConstraint 16 15 31 115.0
ragDoll.addAngularConstraint 32 31 15 115.0

rem ///////////////////////////////////////////////////////////////////////////
rem 
rem			Dihedral angle constraints
rem
rem ///////////////////////////////////////////////////////////////////////////

ragDoll.addDihedralAngleConstraint 47 15 16 19 -10.0
ragDoll.addDihedralAngleConstraint 47 31 32 34 -10.0

ragDoll.addDihedralAngleConstraint 15 1 2 4 -45.0
ragDoll.addDihedralAngleConstraint 31 6 7 9 -45.0

rem ///////////////////////////////////////////////////////////////////////////
rem 
rem			particle-particle distance no less than constraints
rem
rem ///////////////////////////////////////////////////////////////////////////
ragdoll.addDistanceLessThanConstraint 19 1 0.05
ragdoll.addDistanceLessThanConstraint 34 6 0.05

rem ///////////////////////////////////////////////////////////////////////////
rem 
rem			particle-particle distance must equal constraints
rem
rem ///////////////////////////////////////////////////////////////////////////

ragDoll.addConstraint 1 2
ragDoll.addConstraint 47 1
ragDoll.addConstraint 47 6
ragDoll.addConstraint 6 31
ragDoll.addConstraint 7 9
ragDoll.addConstraint 6 7
ragDoll.addConstraint 2 4
ragDoll.addConstraint 32 34
ragDoll.addConstraint 31 32
ragDoll.addConstraint 16 19
ragDoll.addConstraint 15 16
ragDoll.addConstraint 1 31
ragDoll.addConstraint 6 15
ragDoll.addConstraint 1 15
ragDoll.addConstraint 15 31
ragDoll.addConstraint 47 31
ragDoll.addConstraint 47 15
ragDoll.addConstraint 6 1

rem ///////////////////////////////////////////////////////////////////////////
rem 
rem			Bone capsule collision constraints
rem
rem ///////////////////////////////////////////////////////////////////////////
ragDoll.addCapsuleCollision 1 2
ragDoll.addCapsuleCollision 2 4
ragDoll.addCapsuleCollision 6 7
ragDoll.addCapsuleCollision 7 9
ragDoll.addCapsuleCollision 6 31
ragDoll.addCapsuleCollision 1 15
ragDoll.addCapsuleCollision 31 32
ragDoll.addCapsuleCollision 32 34
ragDoll.addCapsuleCollision 15 16
ragDoll.addCapsuleCollision 16 19
ragDoll.addCapsuleCollision 15 31
ragDoll.addCapsuleCollision 1 6



