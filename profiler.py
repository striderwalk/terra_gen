# profiler for project
import cProfile
import os
import pstats

from main import main

with cProfile.Profile() as pr:
    main()
print("timeing ended")

st = pstats.Stats(pr)
st.sort_stats(pstats.SortKey.TIME)
st.print_stats()

try:
    st.dump_stats(filename="data.prof")
    os.system("snakeviz ./data.prof")
except:
    print("exiting bye")
