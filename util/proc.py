import os

def set_lowpriority(pid):
    """ Set the priority a process with pid to below-normal."""

    import sys
    try:
        sys.getwindowsversion()
    except:
        isWindows = False
    else:
        isWindows = True

    if isWindows:
        # Based on:
        #   "Recipe 496767: Set Process Priority In Windows" on ActiveState
        #   http://code.activestate.com/recipes/496767/

        #import win32api,win32process,win32con
        #print("pid: "+str(pid))
        #handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, pid)
        #win32process.SetPriorityClass(handle, win32process.BELOW_NORMAL_PRIORITY_CLASS)

        # currently. on Windows qprocess.pid() returns a void pointer, and not the process id
        # hence, on Windows this is not implemented until finding a proper workaround
        pass
    else:
        import os
        os.system('renice -n 1 -p '+str(pid))
        #os.nice(1)
