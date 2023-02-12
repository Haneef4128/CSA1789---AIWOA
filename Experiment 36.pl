go(Start,Goal) :-
        empty_set(Closed_set),
        empty_pq(Empty_open),
        heuristic(Start, Goal, H),
        insert_pq([Start,nil,0,H,H], Empty_open, Open_list),
        path(Open_list, Closed_set, Goal).
