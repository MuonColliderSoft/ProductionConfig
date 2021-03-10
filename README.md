# ProductionConfig

Production configuration for MuonCollider software.

## Guidelines for new samples
Procedure to share your newly generated sample:
- make sure you collect all information (metadata) needed and detailed in the [Sample description](#-sample-description) section below;
- either fork or create a branch from the master of this repository and add all the configuration files with the convention, with a description in the corresponding `README.md`; see the [Folder Structure](#-folder-structure) section below;
- open a pull request ([help on pull requests](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests)) to the master branch;
- in case of questions or issues, feel free to contact us or open a github issue [here](https://github.com/MuonColliderSoft/ProductionConfig/issues).

## Sample description
A list of available samples can be found here: https://confluence.infn.it/display/muoncollider/Monte+Carlo+Simulated+Samples

and contains the following information:

| Id | CoM Energy (TeV) | Process name | BIB | Events | Software  | Generator (card) | Simulation | Reconstruction | Location | Notes |
|----|------------------|--------------|-----|--------|-----------|------------------|------------|----------------|----------|-------|

where:
- `Id`: represents an unique number associated to the sample;
- `CoM Energy (TeV)` center of mass energy of the hard-scattering process;
- `Process name` is a short description of the physics process (e.g. HH_bbbb, ...);
- `BIB` specifies if beam-induced background is fully included (`1`), partially included (e.g. `0.1` for 10% of expected BIB rate), or not included `0`; if a different configuration (e.g. CoM energy) is used for BIB and hard-scattering, please specify it in the `Notes` column.
- `Events` number of events generated;
- `Software` is the software/detector version, as tagged in the repository and described in the https://confluence.infn.it/display/muoncollider/Releases+notes; if a custom version is used, please add "_custom" to the starting software version, add in the `Notes` what is special and add a link to the relevant code commit, if possible;
- `Generator (card)` is a short name of the folder (see naming convention below) in the repository containing the configuration for the generator/process used (the link should preferably be to a specific commit/version of the card); 
- `Simulation` is a short name of the folder (see naming convention below) in the repository containing the simulation settings and a link to it (the link should preferably be to a specific commit/version of the card);
- `Reconstruction` is a short name of the folder (see naming convention below) in the repository containing the reconstruction settings and a link to it (the link should preferably be to a specific commit/version of the card);
- `Notes` contains any special remark that is deemed useful to know.

## Folder structure
The `simulation` and `reconstruction` folders contain the relevant (mostly XML) configuration files for the respective production step.
The `evtgen` folder contains the run card for the various processes.

Each set of configuration files used for a sample should have its own folder and a `README.md` file, using links in case the files are the same as previous setups, e.g.

```
evtgen
 001-whizard-bbbar
  README.md
  bbbar.sin
  ...
 002-pythia8-4quarkslnu
  README.md
  
 ...
simulation
 001-fullDetector
 002-fullDetector-siDigiDetailed
reconstruction
 001-fullDetector
  reco_steer.xml
  Calo.xml
  Tracking.xml
  LCTuple.xml
  ...
 002-fullDetector -> 001-fullDetector
 003-trkOnly
  reco_steer.xml
  Tracking.xml -> ../001-fullDetector/Tracking.xml
  LCTuple.xml
  ...
 ...
```

For samples using the same configuration, please commit a link (indicated as '->' in the example above) the new folder to the existing one containing the same configuration (git allows to commit links!).

For samples only modifying small parts of the configuration, you can commit links (indicated as '->' in the example above) for all the unchanged files of the configuration you started from.

Please use the `README.md` file to include a longer description of the setup/settings and any relevant note that is useful for reproducing the sample (e.g. for event generation it could include a recipe for sample production, generator version, etc..)

