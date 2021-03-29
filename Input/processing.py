def normalization(trace):
    import numpy as np
    from obspy import Trace
    abs_max_amp = np.max(np.abs(trace.data[:]))
    max_amp = np.max(trace.data[:])
    norm1 = np.abs(trace.data[:]) / abs_max_amp
    norm2 = trace.data[:] ** 2 / max_amp ** 2
    normalized = norm1 - norm2
    trace = Trace(data=normalized, header=(trace.stats))
    return trace


def sta_lta_div (trace, nsta, nlta):
    from obspy import Trace
    import numpy as np

    station = trace.stats.station
    npts = trace.stats.npts
    srt = trace.stats.sampling_rate

    S1 = nlta
    L1 = L2 = S2 = 0
    stlt = np.zeros(npts)
    max = trace.data.argmax()

    while S2 < max:
        S2 = S1 + nsta
        L2 = (S1 + S2) // 2
        L1 = L2 - nlta
        norm1 = np.mean (trace.data[S1:S2] ** 2) ** 2
        norm2 = np.mean (trace.data[L1:L2] ** 2) ** 2
        StaLta = np.round(norm1 / norm2, 3)
        stlt[S1:S2] = StaLta
        S1 += nsta

    data = Trace (data=stlt, header=trace.stats)
    data.taper (max_percentage = 0.1)    
    max = data.data.argmax()
    return max


def envelope(trace):
    from obspy import Trace
    station = trace.stats.station
    npts = trace.stats.npts
    for i in range(1, npts, 1):
        w1 = trace.data[(i - 1)]
        w2 = trace.data[i]
        if w2 <= w1:
            trace.data[i] = w1
        else:
            trace.data[i] = w2

    data = Trace(data=trace.data, header=trace.stats)
    return data
