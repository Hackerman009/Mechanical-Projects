def dms2deg(dms):
    dms = dms.split(sep=".")
    sec = float(str(dms[1][:2]) + "." + str(dms[1][2:]))/3600
    mint = float(str(dms[0][-2:]))/60
    deg = float(str(dms[0][:-2]))
    return deg + mint + sec