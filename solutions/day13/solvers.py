def input_parser(input_data):
    
    # Split into multiple "images" separated by a blank line. Each image
    # itself is a list of multiple lines.
    images = []
    for image in input_data.split('\n\n'):
        images.append(image.splitlines())
    
    return images


def compare_rows(row1, row2, fix_smudge):
    
    if row1 == row2:
        return True, False
    
    if fix_smudge:
        # Check if the rows can be made identical by changing a single
        # character
        smudge_fixed = False
        for i in range(len(row1)):
            if row1[i] == row2[i]:
                continue
            
            if smudge_fixed:
                # A smudge has already been fixed, so the rows aren't equal
                return False, False
            
            smudge_fixed = True
        
        return True, smudge_fixed
    
    return False, False


def find_reflection_point(image, fix_smudges=False):
    
    # Loop through rows in pairs and check for an identical pair
    for i in range(len(image) - 1):
        row1 = image[i]
        row2 = image[i + 1]
        
        rows_match, smudge_fixed = compare_rows(row1, row2, fix_smudges)
        
        if rows_match:
            # The rows match, so check the preceding and succeeding rows to
            # ensure a complete reflection
            prev_row_index = i - 1
            next_row_index = i + 2  # account for row2 already being 1 ahead
            
            while prev_row_index >= 0 and next_row_index < len(image):
                prev_row = image[prev_row_index]
                next_row = image[next_row_index]
                prev_row_index -= 1
                next_row_index += 1
                
                # Only fix the first smudge encountered, and avoid resetting
                # the flag if it was already set
                fix_next_smudge = fix_smudges and not smudge_fixed
                sub_rows_match, sub_smudge_fixed = compare_rows(prev_row, next_row, fix_next_smudge)
                smudge_fixed = smudge_fixed or sub_smudge_fixed
                
                if not sub_rows_match:
                    # This isn't a complete reflection, continue to the next
                    # iteration of the outer loop.
                    break
            else:
                # The loop completed without breaking, so this is a complete
                # reflection. However, if fixing smudges, and no smudge was
                # fixed, it is not the correct reflection.
                if fix_smudges and not smudge_fixed:
                    continue
                
                # Count the number of rows above the line of reflection (i.e.
                # the index at which the reflection was encountered, plus one).
                return i + 1
    
    return None


def part1(input_data, fix_smudges=False):
    
    total = 0
    
    for image in input_data:
        # Check if there is a horizontal reflection
        reflection_point = find_reflection_point(image, fix_smudges=fix_smudges)
        
        if reflection_point is not None:
            total += reflection_point * 100
        else:
            # There wasn't a horizontal reflection point, so check if there is
            # a vertical one, by flipping the image so the columns become rows
            image = list(zip(*image))
            reflection_point = find_reflection_point(image, fix_smudges=fix_smudges)
            total += reflection_point
    
    return total


def part2(input_data):
    
    return part1(input_data, fix_smudges=True)
