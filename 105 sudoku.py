#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 12:11:05 2018

@author: tz
"""

def update_cell(cell, board):
    i,j = cell
    possibles = set([str(k) for k in range(1,10)])
    not_possibles = set([])
    
    # 1. check sub-board
    for ci in range(i//3*3, i//3*3+3):
        for cj in range(j//3*3, j//3*3+3):
            if board[ci][cj].isdigit(): 
                not_possibles.add(board[ci][cj])
                
    # 2. check row
    for ci in range(9):
        if board[ci][j].isdigit():
            not_possibles.add(board[ci][j])
            
    # 3. check column
    for cj in range(9):
        if board[i][cj].isdigit():
            not_possibles.add(board[i][cj])
            
    return cell.extend(list(possibles-not_possibles))
            
def check_board(board):
    
    for iii in [[0,1,2],[3,4,5],[6,7,8]]:
        for jjj in [[0,1,2],[3,4,5],[6,7,8]]:
            subboard = set([])
            for i in iii:
                for j in jjj:
                    if board[i][j].isdigit():
                        if board[i][j] not in subboard: 
                            subboard.add(board[i][j])
                        else:
                            return False
                 
    for i in range(9):
        row = set([])
        for j in range(9):
            if board[i][j].isdigit():
                if board[i][j] not in row:
                    row.add(board[i][j])
                else:
                    return False
  
    for j in range(9):
        col = set([])
        for i in range(9):
            if board[i][j].isdigit():
                if board[i][j] not in col: 
                    col.add(board[i][j])
                else:
                    return False
            
    return True
    
def sudoku_solve(board):
    
    if not check_board(board):
        return Falsed
    
    empties = []
    
    for i in range(9):
        for j in range(9):
            if board[i][j]==".":
                empties.append([i,j])
                
    empties = [update_cell(cell, board) for cell in empties]
    
    empties = sorted(empties, key=len, reverse=True)
    
    if len(empties)==0:
        return True
    
    while empties: 
        empty = empties.pop()
        
        if not check_board(board):
            return False
        
        if len(empty)==2:
            return False
        
        if len(empty)==3:
            i,j,v = empty[0], empty[1], empty[2]
            board[i][j]=str(v)
            empties = [update_cell(cell[:2], board) for cell in empties]
            empties = sorted(empties, key=len, reverse=True)
        
        if len(empty)>3: 

            i,j = empty[0], empty[1]
            votes = []
            for v in empty[2:]:
                board[i][j] = str(v)
                
                votes.append(sudoku_solve(board))
                
                board[i][j] = '.'
            
            if any(votes):
                return True
    return True


board1 = [[".","8","9",".","4",".","6",".","5"],
          [".","7",".",".",".","8",".","4","1"],
          ["5","6",".","9",".",".",".",".","8"],
          [".",".",".","7",".","5",".","9","."],
          [".","9",".","4",".","1",".","5","."],
          [".","3",".","9",".","6",".","1","."],
          ["8",".",".",".",".",".",".",".","7"],
          [".","2",".","8",".",".",".","6","."],
          [".",".","6",".","7",".",".","8","."]]

board2 = [[".",".",".","7",".",".","3",".","1"],
          ["3",".",".","9",".",".",".",".","."],
          [".","4",".","3","1",".","2",".","."],
          [".","6",".","4",".",".","5",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".","1",".",".","8",".","4","."],
          [".",".","6",".","2","1",".","5","."],
          [".",".",".",".",".","9",".",".","8"],
          ["8",".","5",".",".","4",".",".","."]]


print(sudoku_solve(board1))
print(sudoku_solve(board2))