import numpy as np

def dispick(object, vpbeg, wpbeg, deltav):

    nv = np.size(object.traces, axis=0)
    nw = np.size(object.traces, axis=1)
    dispn = np.zeros((nv, nw), dtype=np.float32)
    dispn[:, :] = object.traces[:, :]

    vmin = object.header[0]['f2']
    dv = object.header[0]['d2']
    wmin = object.header[0]['f1']
    dw = object.header[0]['d1']

    ivpbeg = int((vpbeg-vmin)/dv)#+1
    iwpbeg = int((wpbeg-wmin)/dw)#+1
    ideltav = int(deltav/dv)+1
    nvp = int(2.*deltav/dv)+1


    v = np.linspace(vmin, vmin+float(nv-1)*dv, nv)
    w = np.linspace(wmin, wmin+float(nw-1)*dw, nw)

    curve = np.zeros((nw, 2), dtype=np.float32)
    swap = dispn[:,iwpbeg]
    iloc = np.argmax(swap[(ivpbeg-ideltav-1):(ivpbeg+ideltav-1)])
    curve[iwpbeg][1] = v[iloc+ivpbeg-ideltav]
    curve[iwpbeg][0] = w[iwpbeg]
    ivinit = iloc+ivpbeg-ideltav
    ivnew = iloc+ivpbeg-ideltav

    for iw in range(iwpbeg,-1,-1):
        ilocmin = ivnew-ideltav
        ilocmax = ivnew+ideltav
        swap = dispn[:,iw]
        iloc = np.argmax(swap)
        while(iloc < ilocmin or iloc > ilocmax):
            swap[iloc] = 0.
            iloc = np.argmax(swap)
        curve[iw][1] = v[iloc]
        curve[iw][0] = w[iw]
        ivnew = iloc

    ivnew = ivinit

    for iw in range(iwpbeg+1,nw):
        ilocmin = ivnew-ideltav
        ilocmax = ivnew+ideltav
        swap = dispn[:,iw]
        iloc = np.argmax(swap)
        while(iloc < ilocmin or iloc > ilocmax):
            swap[iloc] = 0.
            iloc = np.argmax(swap)
        curve[iw][1] = v[iloc]
        curve[iw][0] = w[iw]
        ivnew = iloc

    return curve
