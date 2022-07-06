# Configuration files that uses ACTs as tracking reconstruction
  
First configuration used with the ACTS tracking


Note that it uses also some specific parameters in the calorimeter section:

## Calo.xml
+    <parameter name="ECALThreshold" type="float">0.002 </parameter>
+    <parameter name="HCALThreshold" type="FloatVec">0.002  </parameter>

## DigiOverlay.xml
+    ECalBarrelCollection          0.25 
+    ECalEndcapCollection          0.25
+    ECalPlugCollection            0.25
 
