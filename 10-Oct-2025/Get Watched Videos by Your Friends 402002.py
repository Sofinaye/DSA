# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
            n = len(friends)
    
            queue = deque()
            visited = [False] * n
            queue.append(id)
            visited[id] = True
            current_level = 0
            while queue and current_level < level:
                level_size = len(queue)
                
                for _ in range(level_size):
                    current_person = queue.popleft()
                    
                    for friend in friends[current_person]:
                        if not visited[friend]:
                            visited[friend] = True
                            queue.append(friend)
                
                current_level += 1
        
            level_people = list(queue)
            video_freq = defaultdict(int)
            for person in level_people:
                for video in watchedVideos[person]:
                    video_freq[video] += 1
            
            sorted_videos = sorted(video_freq.keys())
            result = sorted(sorted_videos, key=lambda video: (video_freq[video], video))
            
            return result