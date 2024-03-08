impl Solution {
    pub fn min_deletion_size(strs: Vec<String>) -> i32 {
        let string_length = strs[0].len();
        let num_strs = strs.len();
        let mut count = 0;

        for i in 0..string_length {
            let mut current = '\0';
            for j in 0..num_strs {
                let c = strs[j].chars().nth(i).unwrap();
                if c < current {
                    count += 1;
                    break;
                } else {
                    current = c;
                }
            }
        }

        count
    }
}
