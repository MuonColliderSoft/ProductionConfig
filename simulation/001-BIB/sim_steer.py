import os

from DDSim.DD4hepSimulation import DD4hepSimulation
from g4units import mm, GeV, MeV, m, deg
SIM = DD4hepSimulation()

## The compact XML file, should be overwrite by command line argument with the right path
SIM.compactFile = "/opt/ilcsoft/muonc/detector-simulation/geometries/MuColl_v1/MuColl_v1.xml"
## Lorentz boost for the crossing angle, in radian!
SIM.crossingAngleBoost = 0.0
SIM.enableDetailedShowerMode = True
SIM.enableG4GPS = False
SIM.enableG4Gun = False
SIM.enableGun = False
## InputFiles for simulation .stdhep, .slcio, .HEPEvt, .hepevt, .hepmc files are supported
SIM.inputFiles = ["seed.slcio"]
## Macro file to execute for runType 'run' or 'vis'
SIM.macroFile = ""
## number of events to simulate, used in batch mode. Simulates all events.
SIM.numberOfEvents = -1
## Outputfile from the simulation,only lcio output is supported: should be overwrite by command line argument
SIM.outputFile = "test.slcio"
## Verbosity use integers from 1(most) to 7(least) verbose or strings: VERBOSE, DEBUG, INFO, WARNING, ERROR, FATAL, ALWAYS
SIM.printLevel = "WARNING"
## The type of action to do in this invocation
SIM.runType = "batch"
## Skip first N events when reading a file
SIM.skipNEvents = 0
## Steering file to change default behaviour
SIM.steeringFile = None
## FourVector of translation for the Smearing of the Vertex position: x y z t
SIM.vertexOffset = [0.0, 0.0, 0.0, 0.0]
## FourVector of the Sigma for the Smearing of the Vertex position: x y z t
SIM.vertexSigma = [0.0, 0.0, 0.0, 0.0]

## set the default tracker action
SIM.action.tracker = "Geant4TrackerWeightedAction"

## set the default calorimeter action
SIM.action.calo = "Geant4ScintillatorCalorimeterAction"

## create a map of patterns and actions to be applied to sensitive detectors
SIM.action.mapActions = {}


################################################################################
## Configuration for the magnetic field (stepper)
################################################################################
SIM.field.delta_chord = 0.25*mm
SIM.field.delta_intersection = 0.001*mm
SIM.field.delta_one_step = 0.01*mm
SIM.field.eps_max = 0.001*mm
SIM.field.eps_min = 5e-05*mm
SIM.field.equation = "Mag_UsualEqRhs"
SIM.field.largest_step = 10.0*m
SIM.field.min_chord_step = 0.01*mm
SIM.field.stepper = "ClassicalRK4"

## default filter for calorimeter sensitive detectors; this is applied if no other filter is used for a calorimeter
SIM.filter.calo = "edep0"

## list of filter objects: map between name and parameter dictionary
SIM.filter.filters = {'edep0': {'parameter': {'Cut': 0.0}, 'name': 'EnergyDepositMinimumCut/Cut0'}, 'geantino': {'parameter': {}, 'name': 'GeantinoRejectFilter/GeantinoRejector'}, 'edep1kev': {'parameter': {'Cut': 0.001}, 'name': 'EnergyDepositMinimumCut'}}

## a map between patterns and filter objects, using patterns to attach filters to sensitive detector
SIM.filter.mapDetFilter = {}

## default filter for tracking sensitive detectors; this is applied if no other filter is used for a tracker
SIM.filter.tracker = "edep1kev"

################################################################################
## Configuration for the DDG4 ParticleGun
################################################################################

## direction of the particle gun, 3 vector
SIM.gun.direction = (0, 0, 1)

## choose the distribution of the random direction for theta
SIM.gun.distribution = None
SIM.gun.energy = 10000.0

## isotropic distribution for the particle gun
SIM.gun.isotrop = False
SIM.gun.multiplicity = 1
SIM.gun.particle = "mu-"
SIM.gun.phiMax = None

## Minimal azimuthal angle for random distribution
SIM.gun.phiMin = None

## position of the particle gun, 3 vector
SIM.gun.position = (0.0, 0.0, 0.0)
SIM.gun.thetaMax = None
SIM.gun.thetaMin = None


################################################################################
## Configuration for the output levels of DDG4 components
################################################################################

## Output level for input sources
SIM.output.inputStage = 3

## Output level for Geant4 kernel
SIM.output.kernel = 3

## Output level for ParticleHandler
SIM.output.part = 3

## Output level for Random Number Generator setup
SIM.output.random = 6


################################################################################
## Configuration for the Particle Handler/ MCTruth treatment
################################################################################

## Keep all created particles
SIM.part.keepAllParticles = False

## Minimal distance between particle vertex and endpoint of parent after
SIM.part.minDistToParentVertex = 2.2e-14

## MinimalKineticEnergy to store particles created in the tracking region
SIM.part.minimalKineticEnergy = 1.0*MeV

## Printout at End of Tracking
SIM.part.printEndTracking = True

## Printout at Start of Tracking
SIM.part.printStartTracking = True

## List of processes to save, on command line give as whitespace separated string in quotation marks
SIM.part.saveProcesses = ['Decay']


################################################################################
## Configuration for the PhysicsList
################################################################################
SIM.physics.decays = False
SIM.physics.list = "QGSP_BERT"

## location of particle.tbl file containing extra particles and their lifetime information
SIM.physics.pdgfile = os.path.join( os.environ.get("DD4HEP"), "DDG4/examples/particle.tbl" )

## The global geant4 rangecut for secondary production
SIM.physics.rangecut = 0.7*mm

SIM.physics.rejectPDGs = {1,2,3,4,5,6,21,23,24,25}

################################################################################
## Properties for the random number generator
################################################################################

## If True, calculate random seed for each event based on eventID and runID
SIM.random.enableEventSeed = False
SIM.random.file = None
SIM.random.luxury = 1
SIM.random.replace_gRandom = True
SIM.random.seed = None
SIM.random.type = None
