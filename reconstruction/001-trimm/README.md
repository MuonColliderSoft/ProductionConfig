## Trimmed process

Configuration file used to overlaid the two bunch crossed (mu+ and mu-) to originated a single BIB. As signal it uses a single muon.

During this process these time cuts (values in ns) are applyed **(-6σ ; +8σ)**:

      VertexBarrelCollection        -0.18 0.24
      VertexEndcapCollection        -0.18 0.24

      InnerTrackerBarrelCollection  -0.36 0.48
      InnerTrackerEndcapCollection  -0.36 0.48

      OuterTrackerBarrelCollection  -0.36 0.48
      OuterTrackerEndcapCollection  -0.36 0.48

      ECalBarrelCollection          -0.25 10.
      ECalEndcapCollection          -0.25 10.
      ECalPlugCollection            -0.25 10.

      HCalBarrelCollection          -0.25 10.
      HCalEndcapCollection          -0.25 10.
      HCalRingCollection            -0.25 10.

      YokeBarrelCollection          -0.25 10.
      YokeEndcapCollection          -0.25 10.

At the end of the process two outputs files are produced with suffix: _trkHits_ and _allHits_

_trkHits_ contains all and only the tracker hits; i.e. the following collections:

InnerTrackerBarrelCollection
InnerTrackerEndcapCollection
OuterTrackerBarrelCollection
OuterTrackerEndcapCollection
VertexBarrelCollection
VertexEndcapCollection


_allHits_ contains all hits; i.e. the following collections:

ECalBarrelCollection
ECalEndcapCollection
HCalBarrelCollection
HCalEndcapCollection
HCalRingCollection
InnerTrackerBarrelCollection
InnerTrackerEndcapCollection
OuterTrackerBarrelCollection
OuterTrackerEndcapCollection
VertexBarrelCollection
VertexEndcapCollection
YokeBarrelCollection
YokeEndcapCollection
