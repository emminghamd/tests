# asks the user to input gpu/cpu temperature and ram usage to give give suggestions based on the inputs
# if the ranges are close to risk zone: gpu: 90-100 / cpu 70-75 / memory 70-75 suggest a course of action in each specific case
# if the ranges are equal or above danger zone: gpu >= 100 (105 for nvidia 110 for AMB) / 80 for CPU >= 80 / memory >= 80 suggest a course of action in each specific case
# RAM: suggest closing browsers/tabs and checking file manager for processes to close if problems persist suggest cleaning the ram and ram docking ports for potential dust the use of Memtest86
# CPU: closing CPU intensive programs, checking if the termal paste is working well (if not reappling it) checking if the cpu fan is working well
# if everything fails or appears as normal but the problem persists suggest the use of best cpu stress test to check for issues, if everything fails suggest that the cpu might be faulty
# GPU: suggest cleaning dust, checking if the GPU dock isn't broken/the vents are working properly 
# if everthing is fine but the temperatures are hot suggest the use of GPU stress tests: FurMark UNIGINE


# case scenario, to monitor a sistem that's under pressure
cpu_temperature = 54
memory_usage = 75
gpu_temperature = 63
print(cpu_temperature > 75 or memory_usage >= 75 or gpu_temperature >= 90)