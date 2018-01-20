#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:11:05 2018

@author: tz
"""
def update_cell(cell, board):
    i,j = cell
    q1 = []; q2 = []; q3 = []
    
    # 1. check sub-board
    for ci in range(i//3*3, i//3*3+3):
        for cj in range(j//3*3, j//3*3+3):
            if board[ci][cj].isdigit(): 
                q1.append(board[ci][cj])
          
    if len(q1) != len(set(q1)): return cell
                
    # 2. check row
    for ci in range(9):
        if board[ci][j].isdigit():
            q2.append(board[ci][j])
     
    if len(q2) != len(set(q2)): return cell
            
    # 3. check column
    for cj in range(9):
        if board[i][cj].isdigit():
            q3.append(board[i][cj])
     
    if len(q3) != len(set(q3)): return cell
    
    cell.extend(list(set([str(k) for k in range(1,10)])-set(q1+q2+q3)))
  
    return cell

def print_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]=='.': pass
    else: 
        for row in board: print(row)
            
def sudoku_solve(board):

    empties = [update_cell([i,j], board) for i in range(9) for j in range(9) if board[i][j]=='.']
    empties = sorted(empties, key=len, reverse=True)
    
    # Exhausts simple choices
    while len(empties[-1])<=3: 
        
        empty = empties.pop()
        i,j = empty[0], empty[1]
        
        if len(empty)==2:
            # The problem is here!
            return False
        
        if len(empty)==3:
            board[i][j]=empty[2]
            empties = [update_cell(cell[:2], board) for cell in empties]
            empties = sorted(empties, key=len, reverse=True)
    print("{} unfilled".format(len(empties)))      
    if len(empties)==0: 
        print_board(board)
        return True
       
    # Deals with multiple choices
    empty = empties.pop()
    i,j = empty[0], empty[1]
    votes = []
    for v in empty[2:]:
        board[i][j] = v
        votes.append(sudoku_solve(board))
        board[i][j] = '.'

    if any(votes):
        return True
    return False

board1 = [[".","8","9",".","4",".","6",".","5"],
          [".","7",".",".",".","8",".","4","1"],
          ["5","6",".","9",".",".",".",".","8"],
          [".",".",".","7",".","5",".","9","."],
          [".","9",".","4",".","1",".","5","."],
          [".","3",".","9",".","6",".","1","."],
          ["8",".",".",".",".",".",".",".","7"],
          [".","2",".","8",".",".",".","6","."],
          [".",".","6",".","7",".",".","8","."]]

#print(update_cell([0,3],board1))
#print(sudoku_solve(board1))

board2 = [[".",".",".","7",".",".","3",".","1"],
          ["3",".",".","9",".",".",".",".","."],
          [".","4",".","3","1",".","2",".","."],
          [".","6",".","4",".",".","5",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".","1",".",".","8",".","4","."],
          [".",".","6",".","2","1",".","5","."],
          [".",".",".",".",".","9",".",".","8"],
          ["8",".","5",".",".","4",".",".","."]]

print(sudoku_solve(board2))