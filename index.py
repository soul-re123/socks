from herbie import Herbie

H = Herbie("2026-11-16 00:00", model= "aigfs", product="sfc", fxx=25)

ds = H.xarray("TMP:2 m")
H.download()

print(ds)