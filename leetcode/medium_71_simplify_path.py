class Solution:
    def simplifyPath(self, path: str) -> str:
        # After looking at the solution, I realized the trick is to use 
        # pyton string SPLIT functionality!!!!
        # "/a//b////c/d//././/..".split('/') 
        # ==> ['', 'a', '', 'b', '', '', '', 'c', 'd', '', '.', '.', '', '..']
        entries = path.split('/')
        print(f'entries={entries}')
        stack = []
        for entry in entries:
            if not entry or entry == '.':
                continue
            # !!!! CANNOT "and stack" here! ".." will get push to stack in case of '/../'!
            # elif entry == '..' and stack:
            elif entry == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(entry)
        # insert '' in the front, otherwise join will not put '/' at root, 
        # also takes care of empty list.
        print(f'stack={stack}')
        if not stack:
            return '/'
        else:
            stack.insert(0, '')
            return '/'.join(stack)
        # IMPORTANT!!!!!!!!
        # stack = ['', 'c'] ==> '/'.join(stack) -> '/c'
        # stack = [''] ==> '/'.join(stack) -> ''
    
        
        # # Following implementation still fails at '////' for example!!!!
        # # Input: "/a/./b/../../c/" => Output: "/c"
        # # Test cases:
        # # "/" => pass
        # # '//' => pass
        # # '/../' => pass
        # # '/./..//././../' => pass
        # stack = []
        # path = path.replace('//', '/')
        # for c in path:
        #     if c == '.':
        #         if stack:
        #             while stack[-1] != '/':
        #                 stack.pop()
        #             stack.pop()  # pop '/'
        #         else:
        #             continue
        #     else:
        #         stack.append(c)
        # if len(stack) > 1 and stack[-1] == '/':  # remove end slash
        #     stack.pop()
        # return ''.join(stack)
        
        # # Following does NOT work!!!!
        # # For example, this does not work for Input: "/a/./b/../../c/" => Output: "/c"
        # # return path.rstrip('/').replace('//', '/').replace('/../', '/')
        # # Note sequence matters!
        # new_path = path.replace('/../', '/').replace('//', '/')
        # return new_path if new_path == '/' else new_path.rstrip('/')

