import lightkurve as lk
import numpy as np

def detrend_data(star_id_list):
    detrended_list = []
    target_id_list =[]   
    sector_list = []
    for i in star_id_list:
        si = str(i)
        id_pre = 'TIC '
        new_star_id = id_pre + si
        lcf = lk.search_lightcurvefile(new_star_id).download_all()        
        for i in lcf:
            hdr = i.header()
            sector = hdr['SECTOR']
            detrended_data = i.PDCSAP_FLUX
            target_id = detrended_data.targetid
            sector_list.append(sector)
            detrended_list.append(detrended_data)
            target_id_list.append(target_id)
        info = np.array([target_id_list,sector_list],np.int32)
    return detrended_list, info