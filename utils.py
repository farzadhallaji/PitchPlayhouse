import re
from pydub import AudioSegment

def time_to_seconds(time_str):
    """Converts a time string MM:SS to seconds."""
    minutes, seconds = map(int, time_str.split(":"))
    return minutes * 60 + seconds

# def parse_string(s):
#     '''
#     example

#     00:00 -> 00:36  5
#     00:36 -> 00:46  5 -> -2
#     00:46 -> 01:02  -2
#     # 00:25 -> 00:32  -12
#     # 00:32 -> 00:39  -12 -> 2
#     # 00:39 -> 01:07  2
#     # 01:02 -> 01:08  -5 -> -12
#     # 01:08 -> 01:14  -12 
#     # 01:14 -> 01:27  -12 -> -5
#     # 01:27 -> 01:32  -5
#     # 01:32 -> 01:35  -5 -> 2
#     # 01:35 -> 01:54  2
#     # 01:54 -> 02:00  2 -> -5
#     # 02:00 -> 02:04  -5
#     # 02:04 -> 02:12  -5 -> 5
#     # 02:12 -> 04:13  8
#     '''
    
#     # Regex pattern to extract the necessary components
#     pattern = r'(\d{2}:\d{2})\s*->\s*(\d{2}:\d{2})\s*(-?\d+)(?:\s*->\s*(-?\d+))?'

#     # Search for the pattern in the string
#     match = re.search(pattern, s)

#     if match:
#         # Extract captured groups
#         start_time, end_time, semitone1, semitone2 = match.groups()
        
#         # If the second semitone is not present, use the first one again
#         semitone2 = semitone2 if semitone2 is not None else semitone1
        
#         return time_to_seconds(start_time), time_to_seconds(end_time), float(semitone1), float(semitone2)
#     else:
#         return None
    


def parse_string(s):
    '''
    example

    00:00 -> 00:36  5.0
    00:36 -> 00:46  5.0 -> -2.5
    00:46 -> 01:02  -2.0
    '''
    
    # Regex pattern to extract the necessary components with float numbers
    pattern = r'(\d{2}:\d{2})\s*->\s*(\d{2}:\d{2})\s*(-?\d+\.\d+)(?:\s*->\s*(-?\d+\.\d+))?'
    # Search for the pattern in the string
    match = re.search(pattern, s)

    if match:
        # Extract captured groups
        start_time, end_time, semitone1, semitone2 = match.groups()
        
        # If the second semitone is not present, use the first one again
        semitone2 = semitone2 if semitone2 is not None else semitone1
        
        return time_to_seconds(start_time), time_to_seconds(end_time), float(semitone1), float(semitone2)
    else:
        return None


# def get_durations_and_values(s):
#     durs = s.split('\n')
#     durations = []
#     semitone_values = []

#     for dur in durs:
#         d0,d1, s0,s1 = parse_string(dur)
#         durations.append((d0,d1))
#         semitone_values.append((s0,s1))
        
#     return durations, semitone_values

def get_durations_and_values(s):
    durations = []
    semitone_values = []
    lines = s.split('\n')
    for line in lines:
        dur = line.strip()
        if dur:
            result = parse_string(dur)
            if result:
                d0, d1, s0, s1 = result
                durations.append((d0, d1))
                semitone_values.append((s0, s1))
    
    return durations, semitone_values

# Utility function to get the duration of an audio file
def get_audio_duration(file_path):
    audio = AudioSegment.from_file(file_path)
    return len(audio) / 1000


