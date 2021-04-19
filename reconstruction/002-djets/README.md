# Reconstruction of dijets using a 3 steps strategy.

## Step1: CaloJet

In the first phase jets are reconstructed using only calorimeter's deposits.

This is the list of processors:

```
<execute>
  <processor name="MyAIDAProcessor"/>
  <processor name="EventNumber" />
  <processor name="Config" />
  <processor name="InitDD4hep"/>
  <processor name="OverlayTrimmed"/> 
  <processor name="MyDDCaloDigi"/>
  <processor name="MyDDSimpleMuonDigi"/>
  <processor name="MyDDMarlinPandora"/>
  <group name="MergeCollections" />
  <group name="PfoSelector" />
  <processor name="MyFastJetProcessor_step1"/>
  <processor name="Output_DST"/>
</execute>
```
The signal's hits are overlayed with the trimmed hits of the BIB (it takes a random BIB beetween the 30 availables), official time cuts are applyed:

```
VertexBarrelCollection -0.18 0.24
VertexEndcapCollection -0.18 0.24
InnerTrackerBarrelCollection -0.36 0.48
InnerTrackerEndcapCollection -0.36 0.48
OuterTrackerBarrelCollection -0.36 0.48
OuterTrackerEndcapCollection -0.36 0.48
ECalBarrelCollection 0.25
ECalEndcapCollection 0.25
ECalPlugCollection 0.25
HCalBarrelCollection 0.25
HCalEndcapCollection 0.25
HCalRingCollection 0.25
YokeBarrelCollection 0.25
YokeEndcapCollection 0.2
```
Jets are built using kt_algorithm with R=0.5

## Step2: regionalTrack

In this step tracks are built using a cone x cone strategy. This means that we limit the tracking to a cone region with R=0.7 around the direction calculated in the previous step, a tracking is perfomed for each jet found in step1.
NB the step requires the new ConformalTracking processor: see https://github.com/MuonColliderSoft/ConformalTracking/tree/conetracking

This is the list pf processors:
```
<execute>
  <processor name="MyAIDAProcessor"/>
  <processor name="EventNumber" />
  <processor name="Config" />
  <processor name="InitDD4hep"/>
  <processor name="VXDBarrelDigitiser"/>
  <processor name="VXDEndcapDigitiser"/>
  <processor name="InnerPlanarDigiProcessor"/>
  <processor name="InnerEndcapPlanarDigiProcessor"/>
  <processor name="OuterPlanarDigiProcessor"/>
  <processor name="OuterEndcapPlanarDigiProcessor"/>
  <processor name="FilterDL_VXDB" />
  <processor name="FilterDL_VXDE" />
  <processor name="MyTruthTrackFinder"/>
  <processor name="ConformalTrackingILC"/>
  <processor name="ClonesAndSplitTracksFinder"/>
  <processor name="Output_DST"/>
</execute>
```
### Tracker hits are first of all digitizied (default parameters) and then filtered with the double layer strategy:
```
<processor name="FilterDL_VXDB" type="FilterDoubleLayerHits">
  <parameter name="DoubleLayerCuts" type="StringVec">
     0 1 0.55 0.3
     2 3 0.55 0.2
     4 5 0.5 0.15
     6 7 0.4 0.12
  </parameter>

<processor name="FilterDL_VXDE" type="FilterDoubleLayerHits">
  <parameter name="DoubleLayerCuts" type="StringVec">
    0 1 0.7 0.11
    2 3 0.7 0.09
    4 5 0.4 0.06
    6 7 0.3 0.042
  </parameter>
```
For the tracking (limited to a cone region) we use a simple strategy in three steps:
```
[VXD]
  @Collections : VXDTrackerHits_DLFiltered
  @Parameters : MaxCellAngle : 0.025; MaxCellAngleRZ : 0.025; Chi2Cut : 100; MinClustersOnTrack : 4; MaxDistance : 0.015; SlopeZRange: 5.0; HighPTCut: 0.5;
  @Flags : HighPTFit
  @Functions : CombineCollections, BuildNewTracks
[VXDALL]
  @Collections : VXDTrackerHits_DLFiltered, VXDEndcapTrackerHits_DLFiltered
  @Parameters : MaxCellAngle : 0.025; MaxCellAngleRZ : 0.025; Chi2Cut : 100; MinClustersOnTrack : 4; MaxDistance : 0.015; SlopeZRange: 10.0; HighPTCut: 0.5;
  @Flags : HighPTFit
  @Functions : CombineCollections, BuildNewTracks
[Tracker]
  @Collections : ITrackerHits, OTrackerHits, ITrackerEndcapHits, OTrackerEndcapHits
  @Parameters : MaxCellAngle : 0.05; MaxCellAngleRZ : 0.05; Chi2Cut : 2000; MinClustersOnTrack : 4; MaxDistance : 0.02; SlopeZRange: 10.0; HighPTCut: 0.5;
  @Flags : HighPTFit, RadialSearch, VertexToTracker
  @Functions : CombineCollections, ExtendTracks
```
## Step3: FullJets

With the last step a full jet reconstruction is done combined tracks and calorimeter's hits.

This is the list pf processors:
```
<execute>
  <processor name="MyAIDAProcessor"/>
  <processor name="EventNumber" />
  <processor name="Config" />
  <processor name="InitDD4hep"/>
  <processor name="Refit" />
  <processor name="MyDDMarlinPandora_2"/>
  <group name="MergeCollections_2" />
  <group name="PfoSelector_2" />
  <processor name="MyFastJetProcessor_step3"/>
  <processor name="Output_REC"/>
  <processor name="Output_DST"/>
</execute>
```

Tracks are then filtered using the Refit processor:
```
<parameter name="DoCutsOnRedChi2Nhits" type="bool"> true </parameter>
<parameter name="ReducedChi2Cut" type="double"> 3. </parameter>
<!--Cuts on Nhits: <detID>,<detID>,... <lower threshold> -->
<parameter name="NHitsCuts" type="StringVec">
  1,2 1
  3,4 1
  5,6 0
</parameter>
```
Jets are built using kt_algorithm with R=0.5
