TWOPHASE = True
DoVOF = True
DoFront = False
GetPropertiesFromFront = False
ZeroReynolds = False
Implicit = False
hypre = False
restart = False
restartFront = False
restartAverages = False
nBackup = 1
NSTEP = 1
EndTime = 1.0
MaxDt = 1e-8
dtFlag = 2
dt = 5e-60
CFL = 0.2
MAXERROR = 1e-5
MAXERRORVOL = 1e-4
ITIME_SCHEME = 1
MAXIT = 50
BETA = 1.2
U_init = 0.e0
termout = 50000
ICOut = True
NOUT = 50000
output_format = 5
out_path = 'out'
nstats = 20
npx = 2
npy = 2
npz = 2
Nx = 20
Ny = 20
Nz = 20
Ng = 2
XLENGTH = 0.5e-4
YLENGTH = 0.5e-4
ZLENGTH = 0.5e-4
read_x = False
read_y = False
read_z = False
x_file = 'xh.dat'
y_file = 'yh.dat'
z_file = 'zh.dat'
xform = 0.0
yform = 0.0
zform = 0.0
GX = 0.0
GY = 0.0
GZ = 0.0
BDRY_COND = {0: 1, 1: 0, 2: 0, 3: 1, 4: 0, 5: 0}
dPdX = -1520000.0
dPdY = 0.0
dPdZ = 0.0
RHO1 = 1000.0
MU1 = 0.001
RHO2 = 1.2
MU2 = 0.00002
SIGMA = 0.072
NumBubble = 1
xyzrad = {(1, 1): 0.25e-4, (2, 1): 0.20e-4, (3, 1): 0.20e-4, (4, 1): 0.1489e-4}
MaxPoint = 2000000
MaxElem = 4000000
MaxFront = 100
amin = 0.32
amax = 0.96
aspmax = 1.54
smooth = True
nsmooth = 10
nregrid = 10
BUOYANCYCASE = 0
