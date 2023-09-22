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

func (s *SinglyLinkedList[T]) GetLastValue() (res T, err error) {
	if s.IsEmpty() {
		return res, errEmptyList
	}
	return s.tail.Value, nil
}

func (s *SinglyLinkedList[T]) GetValues() []T {
	values := make([]T, 0, s.Size())
	current := s.head
	for current != nil {
		values = append(values, current.Value)
		current = current.Next
	}
	current = nil
	return values
}

func (s *SinglyLinkedList[T]) RemoveAt(index int) (res T, err error) {
	if index < 0 || index >= s.count {
		return res, errIndexOutOfBounds
	}

	// only one item
	if s.count == 1 {
		res = s.head.Value
		s.head = nil
		s.tail = nil
		s.count--
		return res, nil
	}

	// delete the first item
	if index == 0 {
		res = s.head.Value
		s.head = s.head.Next
		s.count--
		return res, nil
	}

	// find the previous one node before the target:
	previous, err := s.GetNode(index - 1)
	if err != nil {
		return res, err
	}
	res = previous.Next.Value
	previous.Next = previous.Next.Next

	// if target is the last one node
	if index == s.count-1 {
		// assign the tail to the one node before the last
		s.tail = previous
	}
	s.count--
	return res, nil
}

func (s *SinglyLinkedList[T]) GetNode(index int) (*SLLNode[T], error) {
	if index < 0 || index >= s.count {
		return nil, errIndexOutOfBounds
	}
	/*
		i := 0
		current := s.head
		for current != nil {
			if index == i {
				return current, nil
			}
			current = current.Next
			i++
		}
	*/
	current := s.head
	for i := 0; i < index; i++ {
		current = current.Next
	}
	return current, nil
}

// New generate a singly linked list
func New[T any](values ...T) *SinglyLinkedList[T] {
	s := &SinglyLinkedList[T]{}
	s.Add(values...)
	return s
}
