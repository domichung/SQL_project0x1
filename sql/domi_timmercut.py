def dm_time_cut(_time_str):
    _time_str_cut = [[int(_time_str[i]),int(_time_str[i+1],16)] for i in range(0, len(_time_str), 2)]
    return _time_str_cut