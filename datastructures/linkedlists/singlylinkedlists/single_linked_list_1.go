package singlylinkedlists

import (
	"errors"
)

var (
	errEmptyList        = errors.New("list is empty")
	errIndexOutOfBounds = errors.New("index out of bounds")
)

// SLLNode the node struct of a linked_list
type SLLNode[T any] struct {
	Value T
	Next  *SLLNode[T] // singly linked_list only has next pointer
}

// SinglyLinkedList structure
type SinglyLinkedList[T any] struct {
	count int
	head  *SLLNode[T]
	tail  *SLLNode[T]
}

func (s *SinglyLinkedList[T]) Add(values ...T) {
	for _, value := range values {
		s.InsertAt(s.Size(), value)
	}
}

func (s *SinglyLinkedList[T]) Size() int {
	return s.count
}

func (s *SinglyLinkedList[T]) InsertAt(index int, value T) error {
	if index < 0 || index > s.count {
		return errIndexOutOfBounds
	}
	element := &SLLNode[T]{Value: value}

	if s.IsEmpty() {
		s.head = element
		s.tail = element
		s.count++
		element = nil
		return nil
	}

	if index == 0 {
		element.Next = s.head
		s.head = element
		element = nil
		s.count++
		return nil
	}

	if index == s.count {
		s.tail.Next = element
		s.tail = element
		s.count++
		element = nil
		return nil
	}

	return nil
}

func (s *SinglyLinkedList[T]) IsEmpty() bool {
	return s.Size() == 0
}

func (s *SinglyLinkedList[T]) GetFirstValue() (res T, err error) {
	if !s.IsEmpty() {
		return s.head.Value, nil
	} else {
		return res, errEmptyList
	}
}

// New generate a singly linked list
func New[T any](values ...T) *SinglyLinkedList[T] {
	s := &SinglyLinkedList[T]{}
	s.Add(values...)
	return s
}
